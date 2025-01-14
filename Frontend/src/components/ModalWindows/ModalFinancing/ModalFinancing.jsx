import { useState,useEffect } from 'react';
import styles from './ModalFinancing.module.scss';
import { useSelector } from 'react-redux';

export const ModalFinancing = ({setOpenModalForm ,openModal, setOpenModal, item}) => {

    const lang = useSelector(s =>s.reducer.lang)
    const [data,setData] = useState({})
    const domain = useSelector(s => s.reducer.domain);

    useEffect(()=>{
        (async()=>{
          const res =await fetch(`${domain}/${lang}/api/v1/financing/nameinfo/${item.id}/`,{
            method: 'GET',
            headers: {
                'Content-Type': 'application/json',
            },
          })
          const data_res =await res.json()


          setData(data_res)
        })()
    },[lang])
    const [openDescription, setOpenDescription] = useState(false);


    if(!openModal){
        return <></>;
    }
    return (
        <div onClick={() => {setOpenModal(false); setOpenDescription(false)}} className={styles.open}>

             <div className={styles.open_wrap}>

                <div onClick={event => event.stopPropagation()} className={styles.descriptionBlock}>
                    <div className={styles.img}>
                        <img src={data.name_infos?data.image:''} alt="logo" />
                    </div>
                    <div className={styles.text}>

                        <h2>{data.name_infos?data.name_infos[0].title:''}</h2>
                        <p>{data.name_infos?data.name_infos[0].descriptions:''}</p>

                        <h2>{data.name_infos?data.name_infos[1].title:''}</h2>
                        <p>{data.name_infos?data.name_infos[1].descriptions:''}</p>

                        <h2>{data.name_infos?data.name_infos[2].title:''}</h2>
                        <p>{data.name_infos?data.name_infos[2].descriptions:''}</p>
                    </div>
                </div>

        <div className={styles.button}>
            <button onClick={() => setOpenModalForm(true)} className={styles.callButton}>
                {
                    lang === 'ru'
                    ? 'Связаться'
                    : lang === 'en'
                    ? 'Contact'
                    : 'Байланышуу'
                }
            </button>
        </div>
    </div>
    </div>


    );

}
