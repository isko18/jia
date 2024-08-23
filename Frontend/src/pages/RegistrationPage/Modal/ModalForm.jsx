import { useSelector } from "react-redux";
import { useState, useEffect } from "react";
import axios from "axios";

const inputList = [
    {
        tag: 'text',
        ru: 'Ваше полное имя',
        en: 'Your full name',
        ky: 'Аты-жөнү'
    },
    {
        tag: 'text',
        ru: 'Название компании',
        en: 'Company name',
        ky: 'Компаниянын аталышы'
    },
    {
        tag: 'select',
        ru: 'Укажите сектор',
        en: 'Select your sector',
        ky: 'Секторду көрсөтүңүз'
    },
    {
        tag: 'other',
        ru: 'Другое',
        en: 'Other',
        ky: 'Башка'
    },
    {
        tag: 'number',
        ru: 'Количество билетов',
        en: 'Number of tickets',
        ky: 'Билеттердин саны'
    },
    {
        tag: 'email',
        ru: 'Электронная почта',
        en: 'Email',
        ky: 'Электрондук почта'
    },
    {
        tag: 'tel',
        ru: 'Номер телефона',
        en: 'Phone number',
        ky: 'Телефон номуру'
    },
]


const ModalForm = ({setSelectedForm, showModal}) => {
    const lang = useSelector(s => s.reducer.lang);
    const domain = useSelector(s => s.reducer.domain);
    const [sectorList, setSectorList] = useState([]);
    const [full_name, setFull_name] = useState('');
    const [name_company, setName_company] = useState('');
    const [sector_id, setSector_id] = useState('');
    const [sector_text, setSector_text] = useState('');
    const [current, setCurrent] = useState('');
    const [email, setEmail] = useState('');
    const [phone, setPhone] = useState('');
    

    function getCsrfToken() {
        const name = 'csrftoken=';
        const decodedCookie = decodeURIComponent(document.cookie);
        const cookies = decodedCookie.split(';');
        for(let i = 0; i < cookies.length; i++) {
          let cookie = cookies[i].trim();
          if (cookie.indexOf(name) === 0) {
            return cookie.substring(name.length, cookie.length);
          }
        }
        return '';
      }

    const sendFormData = () =>{
        console.log({
            full_name,
            name_company,
            sector:
            sector_text
            ? sector_text
            : sector_id,
            current,
            email,
            phone
        });

        axios.post(
            showModal === 'vip'
            ? `${domain}/ru/api/v1/registration/reach_vip/`
            : `${domain}/ru/api/v1/registration/reach-standart/`,
            {
                full_name,
                name_company,
                sector:
                sector_text
                ? sector_text
                : sector_id,
                current,
                email,
                phone
            },  {
                headers: {
                  'X-CSRFToken': getCsrfToken(),
                },
              }
        )
        .then(response =>{
            console.log(response)
             setSelectedForm(2)
        })
        .catch(error => {
            console.log(error);
            alert('Что-то пошло не так или вы не заполнили все поля(')
        })
        .finally(()=>{

        })
    }

    const formTitle = showModal === 'vip'
    ? 'Форма бронирования для VIP пакета'
    : 'Форма бронирования для Стандартного пакета';

    useEffect(()=>{

        const csrfToken = getCsrfToken();
        axios.interceptors.request.use((config) => {
          config.headers['X-CSRF-TOKEN'] = csrfToken;
          return config;
        }, (error) => {
          return Promise.reject(error);
        });

        axios(
            showModal === 'vip'
            ? `${domain}/ru/api/v1/registration/sector_vip/`
            : `${domain}/ru/api/v1/registration/sector-standart/`
        )
        .then(({data}) =>{
            setSectorList(data)
        })
        .catch(error => {
            console.log(error);
        })

    }, [])


    return (
        <div className="registration-modal-form-wrapper" onClick={(event)=>{
            event.stopPropagation()
        }}>
            <form className="registration-modal-form" onSubmit={e => e.preventDefault()}>
            <h1 className="registration-modal-form-title">{formTitle}</h1>

            <input
                        onChange={e=>{
                            setFull_name(e.target.value)
                        }}
                        required={true}
                         placeholder={inputList[0][lang]}
                         type={'text'}
                         className="registration-modal-form-input" />
                           <input
                        onChange={e=>{
                            setName_company(e.target.value)
                        }}
                        required={true}
                         placeholder={inputList[1][lang]}
                         type={'text'}
                         className="registration-modal-form-input" />
                          <select onChange={e => {
                        setSector_id(e.target.value);
                        setSector_text('')
                    }}
                       required={true}
                        defaultValue={0}
                         className="registration-modal-form-input">

                        <option value="0" disabled={true}>{inputList[2][lang]}</option>
                        {
                            sectorList.map(item =>{
                                return <option key={item.id} value={item.name}>{item.name}</option>
                            })
                        }
                            <option value="other">{
                                lang === 'ru'
                                ? 'Другое'
                                : lang === 'en'
                                ? 'Other'
                                : 'Башка'
                                }</option>
                    </select>
                          {
                            sector_id === 'other'
                            ?  <input
                            onChange={e=>{
                                setSector_text(e.target.value)
                            }}
                            required={true}
                             placeholder={inputList[3][lang]}
                             type={'text'}
                             className="registration-modal-form-input" />
                             : ''
                          }

                           <input
                        onChange={e=>{
                            setCurrent(e.target.value)
                        }}
                        required={true}
                         placeholder={inputList[4][lang]}
                         type={'tnumber'}
                         className="registration-modal-form-input" />
                           <input
                        onChange={e=>{
                            setEmail(e.target.value)
                        }}
                        required={true}
                         placeholder={inputList[5][lang]}
                         type={'email'}
                         className="registration-modal-form-input" />
                          <input
                        onChange={e=>{
                            setPhone(e.target.value)
                        }}
                        required={true}
                         placeholder={inputList[6][lang]}
                         type={'tel'}
                         className="registration-modal-form-input" />
            {
                // inputList.map((item, idx) =>{

                //     if(item.tag === 'other' && sector_id !== 'other') return ''
                //      if (item.tag === 'select'){
                //       return
                //     } else{

                //         return <input
                //         onChange={e=>{
                //             stateList[idx].setState(e.target.value)
                //         }}
                //         key={item.en}
                //         required={true}
                //          placeholder={item[lang]}
                //          type={item.tag}
                //          className="registration-modal-form-input" />
                //     }
                // })
            }


            </form>
            <button className="registration-modal-form-btn registration-modal-btn"
            onClick={()=>{
                sendFormData()

            }}
            >{
                lang === 'ru'
                ? 'Отправить'
                : lang === 'en'
                ? 'Send'
                : 'Тапшыруу'
            }</button>
        </div>
    );
}

export default ModalForm;
