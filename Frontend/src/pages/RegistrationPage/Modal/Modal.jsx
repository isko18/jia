import './modal.scss';
import ModalForm from './ModalForm';
import ModalQR from './ModalQR';
import ModalComplete from './ModalComplete';
import { useState } from 'react';

const Modal = ({setShowModal, showModal}) => {
    const [selectedForm, setSelectedForm] = useState(1);
    return (
        <div className="registration-modal-wrapper" onClick={()=>{
            setShowModal(false)
        }}>

            {
                selectedForm === 1
                ? <ModalForm showModal={showModal} setSelectedForm={setSelectedForm} />
                : selectedForm === 2
                ? <ModalQR setSelectedForm={setSelectedForm} />
                : <ModalComplete />
            }
        </div>
    );
}

export default Modal;
