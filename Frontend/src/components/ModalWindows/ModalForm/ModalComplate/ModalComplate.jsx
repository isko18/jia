import { Link } from 'react-router-dom';
import styles from './ModalComplate.module.scss';
import { useSelector } from 'react-redux';

export const ModalComplate = ({ openModalComplate, setOpenModalComplate }) => {
    const lang = useSelector(s => s.reducer.lang)
    if(!openModalComplate)  {
        return null;
    }
    return (
        <div onClick={() => setOpenModalComplate(!openModalComplate)} className={styles.open}>
            <div onClick={event => event.stopPropagation()} className={styles.block}>
                <h2 className={styles.completeText}>
                    {
                        lang === 'ru'
                        ? 'Ваш запрос получен, с Вами свяжутся!'
                        : lang === 'en'
                        ? 'Your request has been received, you will be contacted!'
                        : 'Өтүнүчүңүз кабыл алынды жана сиз менен байланышат!'
                    }
                </h2>
            </div>
            <div className={styles.button}>
                <Link to={'/'}><button className={styles.callButton}>{
                    lang === 'ru'
                    ? 'На главную'
                    : lang === 'en'
                    ? 'To the main page'
                    : 'Башкы бетке'
                    }</button></Link>
            </div>
        </div>
    );
}
