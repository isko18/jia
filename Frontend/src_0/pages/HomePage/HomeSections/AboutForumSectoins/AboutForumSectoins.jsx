import { useEffect, useRef, useState } from 'react';
import styles from './AboutForumSectoins.module.scss';
import { ModalSendForm } from '@components/index';
import axios from 'axios';
import { useSelector } from 'react-redux';

export const AboutForumSectoins = () => {
    const lang = useSelector((s) => s.reducer.lang);
    const [text, setText] = useState({});
    const [statistic, setStatistic] = useState([]);
    const [buttonText, setButtonText] = useState({});
    const [currVal1, setCurrVal1] = useState(0);
    const [currVal2, setCurrVal2] = useState(0);
    const [currVal3, setCurrVal3] = useState(0);
    const domain = useSelector(s => s.reducer.domain);


    const observerRef = useRef(null);
    const [openModal, setOpenModal] = useState(false);

    useEffect(() => {
        axios.get(`${domain}/${lang}/api/v1/base/about_the_forum/`)
            .then(({ data }) => setText(data[0]))
            .catch((error) => console.error('Error fetching about the forum data:', error));

        axios.get(`${domain}/${lang}/api/v1/about/statistics/`)
            .then(({ data }) => {
                setStatistic(data);
                if (data.length >= 3) {
                    setCurrVal1(0);
                    setCurrVal2(0);
                    setCurrVal3(0);
                }
            })
            .catch((error) => console.error('Error fetching statistics data:', error));

        axios.get(`${domain}/${lang}/api/v1/base/button/`)
            .then(({ data }) => setButtonText(data[0]))
            .catch((error) => console.error('Error fetching button text data:', error));
    }, [lang, domain]);

    useEffect(() => {
        const currentRef = observerRef.current;

        const observer = new IntersectionObserver(
            (entries) => {
                const entry = entries[0];
                if (entry.isIntersecting && statistic.length >= 3) {
                    const targetVal1 = Number(statistic[0].title.split(" ")[0]);
                    const targetVal2 = Number(statistic[1].title.split(" ")[0]);
                    const targetVal3 = Number(statistic[2].title.split(" ")[0]);

                    const duration = 2000;
                    const steps = 100;
                    const interval = duration / steps;

                    const increment1 = targetVal1 / steps;
                    const increment2 = targetVal2 / steps;
                    const increment3 = targetVal3 / steps;

                    let count = 0;

                    const intervalId = setInterval(() => {
                        count++;
                        setCurrVal1((prev) => Math.min(prev + increment1, targetVal1));
                        setCurrVal2((prev) => Math.min(prev + increment2, targetVal2));
                        setCurrVal3((prev) => Math.min(prev + increment3, targetVal3));

                        if (count >= steps) {
                            clearInterval(intervalId);
                            setCurrVal1(targetVal1);
                            setCurrVal2(targetVal2);
                            setCurrVal3(targetVal3);
                        }
                    }, interval);
                }
            },
            {
                threshold: 0.9,
            }
        );

        if (currentRef) {
            observer.observe(currentRef);
        }

        return () => {
            if (currentRef) {
                observer.unobserve(currentRef);
            }
        };
    }, [statistic]);

    return (
        <section className='container'>
            <div className={styles.container}>
                <h2>{text.title}</h2>
                <p>{text.descriptions}</p>

                <div ref={observerRef} className={styles.flexItems}>


                    <div className={styles.item}>
                        <h3>
                            {Math.floor(currVal1)}{statistic[0]?.title.split(" ").slice(1).join(" ")}
                        </h3>
                        <p>{statistic[0]?.descriptions}</p>
                    </div>
                    <div className={styles.item}>
                        <h3>
                            {Math.floor(currVal2)}{statistic[1]?.title.split(" ").slice(1).join(" ")}
                        </h3>
                        <p>{statistic[1]?.descriptions}</p>
                    </div>
                    <div className={styles.item}>
                        <h3>
                            {Math.floor(currVal3)}{statistic[2]?.title.split(" ").slice(1).join(" ")}
                        </h3>
                        <p>{statistic[2]?.descriptions}</p>
                    </div>
                </div>

                <button onClick={() => setOpenModal(!openModal)} className={styles.button}>
                    {buttonText.title}
                </button>
            </div>
            <ModalSendForm openModal={openModal} setOpenModal={setOpenModal} />
        </section>
    );
};
