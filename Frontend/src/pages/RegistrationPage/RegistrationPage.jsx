import './registrationPage.scss';
import Modal from './Modal/Modal';
import { useState, useEffect } from 'react';
import axios from 'axios';
import { useSelector } from 'react-redux';

 export const RegistrationPage = () => {
    const lang = useSelector(s => s.reducer.lang);
    const domain = useSelector( s => s.reducer.domain);
    const [showModal, setShowModal] = useState('');
    const [text, setText] = useState('');
    const [titleStandart, setTitleStandart] = useState('');
    const [titleVip, setTitleVip] = useState('');
    const [textStandart, setTextStandart] = useState('');
    const [textVip, setTextVip] = useState('');

    useEffect(()=>{
        axios(`${domain}/${lang}/api/v1/registration/registration/`)
        .then(({data}) => setText(data[0]));

        axios(`${domain}/${lang}/api/v1/registration/sector-standart/1/`)
        .then(({data})=> setTitleStandart(data));

        axios(`${domain}/${lang}/api/v1/registration/sector_vip/1/`)
        .then(({data})=> setTitleVip(data));

        axios(`${domain}/${lang}/api/v1/registration/standart/`)
        .then(({data}) => setTextStandart(data[0]));
        axios(`${domain}/${lang}/api/v1/registration/vip/`)
        .then(({data}) => setTextVip(data[0]));

    },[lang])
    return (
        <div className='registration'  style={{ minHeight: '100vh'}}>
            {
                showModal
                ? <Modal showModal={showModal} setShowModal={setShowModal} />
                : ''
            }
            <div className="container">
                    <h1 className="registration-title">{text.title}</h1>
                    <p className="registration-text">{text.descriptions}</p>
                    <div className="row">
                        <div className="col-6">
                            <div className="registration-widget">
                               <div className="registration-widget-text-bock">
                               <h4 className="registration-widget-title">{titleStandart.name}</h4>
                               <div className="registration-widget-text" dangerouslySetInnerHTML={{__html:textStandart.descriptions}}></div>

                               </div>

                                    <button className="registration-widget-btn"
                                    onClick={()=>{
                                        setShowModal('base')
                                    }}
                                    >{
                                        lang === 'ru'
                                        ? 'Забронировать стандартный пакет'
                                        : lang === 'en'
                                        ? 'Book a standard package'
                                        : 'Стандарттык пакетти ээлеп коюу'
                                    }</button>
                            </div>
                        </div>

                        <div className="col-6">
                            <div className="registration-widget">
                                <div className="registration-widget-text-bock">
                                <h4 className="registration-widget-title registration-widget-title-gold">{titleVip.name}</h4>
                                <div className="registration-widget-text" dangerouslySetInnerHTML={{__html:textVip.descriptions}}>
                                </div>

                                </div>

                                    <button className="registration-widget-btn"
                                     onClick={()=>{
                                        setShowModal('vip')
                                    }}
                                    >
                                        {
                                        lang === 'ru'
                                        ? 'Забронировать VIP пакет'
                                        : lang === 'en'
                                        ? 'Book a VIP package'
                                        : 'VIP пакетти ээлеп коюу'
                                    }
                                        </button>
                            </div>
                        </div>
                    </div>
            </div>
        </div>
    );
}
