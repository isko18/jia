import "./header.scss";
import { Link } from "react-router-dom";
import bifIcon from "./icons/bifIcon.svg";
import bifMobileIcon from './icons/bifMobileIcon.svg';
import arrow from "../../img/header/Icons.svg";
import { useState, useEffect } from "react";
import { useMediaQuery } from "@hooks/usemedia/useMedia";
import { setLang } from "../../redux/reducer";
import { useDispatch, useSelector } from "react-redux";
import burgerIcon from './icons/burger-icon.svg';
import axios from "axios";
import greenIcon2 from './icons/greenEconomyIcon2.svg';

const languages = [
  {
    id: 1,
    value: "ru",
    text: "Рус",
  },
  {
    id: 2,
    value: "en",
    text: "Eng",
  },
  {
    id: 3,
    value: "ky",
    text: "Кыр",
  },
];

const linkText = {
  main:{
    ru: 'Главная',
    en: 'Home',
    ky: 'Башкы бет',
  },
  projects:{
    ru: 'О проекте',
    en: 'About project',
    ky: 'Долбоор жөнүндө',
  },
  funds:{
    ru: 'Источники финансирования',
    en: 'Sources of financing',
    ky: 'Каржылоо булактары',
  },
  business:{
    ru: 'Бизнес проекты',
    en: 'Business projects',
    ky: 'Бизнес долбоорлор',
  },
  exhibition:{
    ru: 'Выставка',
    en: 'Exhibition',
    ky: 'Көргөзмө',
  },
}


export const Header = () => {
  const [showLangList, setShowLangList] = useState(false);
  const [selectedLang, setSeletedLang] = useState(languages[0]);
  const dispatch = useDispatch();
  const lang = useSelector(s => s.reducer.lang);
  const [showBurger, setShowBurger] = useState(false);
  const [logo, setLogo] = useState({})
  const domain = useSelector(s => s.reducer.domain);
  const scrollToTop = () => {
    window.scrollTo({
      top: 0,
      behavior: "smooth",
    });
  };

  const showLang = () => {
    setShowLangList(!showLangList);
  };

const burgerFunc = () =>{

  if(showBurger){
     document.querySelector('body').style.cssText = 'overflow: auto;'
  } else{
     document.querySelector('body').style.cssText = 'overflow: hidden;'
  }
  setShowBurger(!showBurger);

}

  const w = useMediaQuery("(min-width: 1024px)");
  useEffect(()=>{
    dispatch(setLang(selectedLang.value))
  }, [selectedLang, dispatch])

  useEffect(()=>{
    axios(`${domain}/ru/api/v1/base/logo/`)
    .then(({data})=> setLogo(data[0]))
    .catch((error) => {
      setLogo({})
    });
  }, [])
  return (
    <header>
      <div className={"header-top"}>
        <div className="container">
          <div className="header-top-container">
            <div className="header-top-img header-top-img-1">
              <img  className="header-top-img-img1" src={
                window.screen.width > 576
                ? bifIcon
                : bifMobileIcon
              } alt="" />
            </div>
            {
              logo.logo_2
              ? <div className="header-top-img header-top-img2">
                <img src={greenIcon2} alt="" className="header-top-img-2" />
              <img className="header-top-img-img2" src={logo.logo_2} alt="" />
            </div>
            : ''
            }

          </div>
        </div>
      </div>

      <div className="header">
        <div className="container header-container">
          <div className="header-menu">
            <div className="burger-btn" onClick={()=>{
              burgerFunc()

            }}>
                <img src={burgerIcon} alt="" />
            </div>
            <div className={
              showBurger
              ? 'header-nav-show-bg header-nav-show-bg-show'
              : 'header-nav-show-bg'
            } onClick={()=>{
              burgerFunc()
            }}></div>

<div className={'header-nav header-nav-desktop'}>


            <Link onClick={()=>{
              scrollToTop();
            }} to={"/"}>
              {linkText.main[lang]}
            </Link>
            <Link  onClick={()=>{
              scrollToTop();
            }} to={"/projects"}>
             {linkText.projects[lang]}
            </Link>
            <Link onClick={()=>{
              scrollToTop();
            }} to={"/funds"}>
              {linkText.funds[lang]}
            </Link>
            <Link  onClick={()=>{
              scrollToTop();
            }} to={"/business"}>
              {linkText.business[lang]}
            </Link>
            <Link  onClick={()=>{
              scrollToTop();
            }} to={"/exhibition"}>
              {linkText.exhibition[lang]}
            </Link>
          </div>

          <div className={
            showBurger
            ? "header-nav header-nav-mobile header-nav-show"
            : "header-nav header-nav-mobile"
          }>

            <button className="close-burger-btn" onClick={()=>{
             burgerFunc()
            }}></button>
            <Link onClick={()=>{
              scrollToTop();
              burgerFunc()
            }} to={"/"}>
              {linkText.main[lang]}
            </Link>
            <Link  onClick={()=>{
              scrollToTop();
              burgerFunc()
            }} to={"/projects"}>
             {linkText.projects[lang]}
            </Link>
            <Link onClick={()=>{
              scrollToTop();
              burgerFunc()
            }} to={"/funds"}>
              {linkText.funds[lang]}
            </Link>
            <Link  onClick={()=>{
              scrollToTop();
              burgerFunc()
            }} to={"/business"}>
              {linkText.business[lang]}
            </Link>
            <Link  onClick={()=>{
              scrollToTop();
              burgerFunc()
            }} to={"/exhibition"}>
              {linkText.exhibition[lang]}
            </Link>
          </div>
          </div>

          <div className="header-lang" onClick={showLang}>
            <div className="header-lang-text">{selectedLang.text}</div>
            <img src={arrow} alt="" className="header-lang-icon" />
            <div className={
              showLangList
              ? 'header-lang-list header-lang-list-show'
              : 'header-lang-list'
            }>
              {
                languages.filter(item => item.id !== selectedLang.id).map(item =>{
                  return <p key={item.id} className="header-lang-text" onClick={()=>{
                    setSeletedLang(item)
                  }}>{item.text}</p>
                })
              }
            </div>
          </div>
        </div>
      </div>
    </header>
  );
};
