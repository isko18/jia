import React, { useState, useEffect } from 'react';
import { useSelector } from 'react-redux';
import axios from 'axios';
import ReactPlayer from 'react-player';
import styles from './VideosSection.module.scss';
import border1 from '@img/videoSec1.svg';
import border2 from '@img/videoSec2.svg';
import border3 from '@img/videoSec3.svg';
import border_response1 from '@img/border_response.svg';
import border_response_mobile1 from '@img/border_response_mobile.svg';
import bifLogo from './img/bifLogo.svg';
import greenLogo from './img/greenLogo.svg';

export const VideosSection = () => {
    const lang = useSelector(s => s.reducer.lang);
    const [videoData, setVideoData] = useState([]);
    const [logo, setLogo] = useState(null); // Initialize as null to handle loading state
    const domain = useSelector(s => s.reducer.domain);
    useEffect(() => {
        const fetchVideoData = async () => {
            try {
                const response = await axios(`${domain}/${lang}/api/v1/base/video/`);
                setVideoData(response.data);
            } catch (error) {
                console.error('Error fetching video data:', error);
            }
        };

        fetchVideoData();
    }, [lang, domain]);

    useEffect(() => {
        const fetchLogoData = async () => {
            try {
                const response = await axios(`${domain}/ru/api/v1/base/logo/`);
                setLogo(response.data[0]);
            } catch (error) {
                console.error('Error fetching logo data:', error);
                setLogo(null); // Set to null in case of error
            }
        };

        fetchLogoData();
    }, [domain]);

    const viewportWidth = window.innerWidth;
    const videoWidth = viewportWidth > 768 ? '640px' : '100%';

    return (
        <section className={styles.container}>
            <div className={styles.whiteBlock}>
                <div className={`${styles.center} container`} style={{ position: 'relative' }}>
                    <img src={border1} alt="Border 1" className={styles.border1} />
                    <img src={border2} alt="Border 2" className={styles.border2} />
                    <img src={border3} alt="Border 3" className={styles.border3} />
                    <img src={border_response1} alt="Border Response" className={styles.border_response} />
                    <img src={border_response_mobile1} alt="Border Response Mobile" className={styles.border_response_mobile} />
                    <img src={bifLogo} alt="BIF Logo" className={styles.bifLogo} />
                    {logo?.logo_2 && <img src={greenLogo} alt="Green Logo" className={styles.greenLogo} />}
                    {videoData.map((item, idx) => (
                        <div key={item.id || idx} className={styles.blockVideo}>
                            {idx % 2 === 0 ? (
                                <>
                                    <div className={styles.text}>
                                        <h2>{item.title}</h2>
                                        <p dangerouslySetInnerHTML={{ __html: item.descriptions }} />
                                    </div>
                                    <ReactPlayer
                                        controls
                                        url={item.url}
                                        width={videoWidth}
                                        style={{ position: 'relative' }}
                                    />
                                </>
                            ) : (
                                <>
                                    <ReactPlayer
                                        controls
                                        url={item.url}
                                        width={videoWidth}
                                        style={{ position: 'relative' }}
                                    />
                                    <div className={styles.text}>
                                        <h2>{item.title}</h2>
                                        <p dangerouslySetInnerHTML={{ __html: item.descriptions }} />
                                    </div>
                                </>
                            )}
                        </div>
                    ))}
                </div>
            </div>
        </section>
    );
};
