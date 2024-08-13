import styles from './FirstSection.module.scss';
import graph from '@img/graph.png';
import logo from '@img/header/GreenEconomy1.png'
import { useState, useEffect } from 'react';
import { ModalFinancing } from '@components/index';
import { ModalForm } from '@components/ModalWindows/ModalForm/ModalForm';
import { ModalComplate } from '@components/ModalWindows/ModalForm/ModalComplate/ModalComplate';
import axios from 'axios';
import { useSelector } from 'react-redux';

export const FirstSection = () => {
    const lang = useSelector(s => s.reducer.lang);
    const [openModal, setOpenModal] = useState(false);
    const [openModalForm, setOpenModalForm] = useState(false);
    const [complate, setComplate] = useState(false);
    const [item,setItem] = useState(null);
    const [arrTable, setArrTable] = useState([]);
    const domain = useSelector(s => s.reducer.domain);




  useEffect(()=>{
    axios(`${domain}/${lang}/api/v1/financing/image/`)
    .then(({data})=> setArrTable(data))
  }, [lang]);
    return (
        <section className='container'>
            <div className={styles.container}>
                <div className={styles.logoContainer}>
                    {
                        arrTable?.map(item => (
                        <div onClick={() => {setOpenModal(!openModal);setItem(item)}} className={styles.logoItem} key={item.id}>
                                <img className={styles.img} src={item.image} alt="logo" />
                            </div>
                        ))
                    }
                </div>
               {
                openModal?
                <ModalFinancing setOpenModalForm={setOpenModalForm} item={item} openModal={openModal} setOpenModal={setOpenModal} />
                :''
               }
                <button onClick={() => setOpenModalForm(!openModalForm)} className={styles.button}>
                {
                    lang === 'ru'
                    ? 'Связаться'
                    : lang === 'en'
                    ? 'Contact'
                    : 'Байланышуу'
                }
                </button>
                <ModalForm openModalForm={openModalForm} setOpenModalForm={setOpenModalForm} setComplate={setComplate}/>
                <ModalComplate openModalComplate={complate} setOpenModalComplate={setComplate} />
            </div>
        </section>
    );
}
