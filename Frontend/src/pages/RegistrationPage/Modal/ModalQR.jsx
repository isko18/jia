import qr from "../img/QR.png";
import { useSelector } from "react-redux";

const ModalQR = ({ setSelectedForm }) => {
  const lang = useSelector(s => s.reducer.lang);

  return (
    <div
      className="registration-modal-qr-wrapper"
      onClick={(e) => e.stopPropagation()}
    >
      <div className="registration-modal-qr-block">
        <img className="registration-modal-qr-img" src={qr} alt="" />
        <p className="registration-modal-qr-text">
        {
                lang === 'ru'
                ? 'Пожалуйста, сохраните чек за покупку билета'
                : lang === 'en'
                ? 'Please keep your ticket purchase receipt.'
                : 'Билет сатып алган квитанцияңызды сактап коюңуз.'
            }
        </p>
      </div>
      <button
        className="registration-modal-btn"
        onClick={() => {
          setSelectedForm(3);
        }}
      >
        {
                lang === 'ru'
                ? 'Оплатил'
                : lang === 'en'
                ? 'Paid'
                : 'Төлөндү'
            }

      </button>
    </div>
  );
};

export default ModalQR;
