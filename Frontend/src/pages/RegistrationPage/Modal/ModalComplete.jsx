import completeIcon from '../img/complete-icon.svg';
import { useNavigate } from 'react-router-dom';
import { useSelector } from 'react-redux';

const ModalComplete = () => {
    const navigate = useNavigate();
    const lang = useSelector(s => s.reducer.lang);
    const scrollToTop = () => {
        window.scrollTo({
          top: 0,
          behavior: "smooth",
        });
      };
    return (
        <div className="registration-modal-complete-wrapper" onClick={ e => e.stopPropagation()}>
            <div className="registration-modal-complete-block">
                    <img src={completeIcon} alt="" className="registration-modal-complete-img" />
                    <h4 className="registration-modal-complete-title">{
                        lang === 'ru'
                        ? 'Спасибо за ваше бронирование! С Вами свяжутся организаторы.'
                        : lang === 'en'
                        ? 'Thank you for your booking! The organizers will contact you.'
                        : 'Резервиңиз үчүн рахмат! Уюштуруучулар сиз менен байланышат.'
                        }</h4>
                    <p className="registration-modal-complete-text">
                        {
                            lang === 'ru'
                            ? 'В случае необходимости дополнительных данных или разъяснений, обращаться к по номеру (WhatsApp)'
                            : lang === 'en'
                            ? 'If you need additional information or clarification, please contact us by phone (WhatsApp)'
                            : 'Кошумча маалымат же тактоо керек болсо, байланышыңыз  (WhatsApp)'
                        }
                         <a target='_blank' rel="noreferrer" href="https://api.whatsapp.com/send?%20phone=996555895362"> +996 555 895 362</a>
                         </p>
            </div>
            <button className="registration-modal-btn"
                onClick={()=>{
                    navigate(`/${lang}`);
                    scrollToTop()
                }}
            >{
                lang === 'ru'
                ? 'На главную'
                : lang === 'en'
                ? 'To the main page'
                : 'Башкы бетке'
            }</button>
        </div>
    );
}

export default ModalComplete;
