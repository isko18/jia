import "./exhibition.scss";
import ExhibitionSlider from "./ExhibitionSlider";
import axios from "axios";
import { useState, useEffect } from "react";
import { useSelector } from "react-redux";
import borderLeftIcon from './img/border-left.svg';
import borderRightIcon from './img/border-right.svg';


export const ExhibitionPage = () => {
  const [text, setText] = useState({});
  const lang = useSelector((s) => s.reducer.lang);
  const domain = useSelector(s => s.reducer.domain);

  useEffect(() => {
    setText({});
    axios(`${domain}/${lang}/api/v1/exhibition/exhibitions/`).then(
      ({ data }) => setText(data[0])
    );
  }, [lang, domain]);
  return (
    <div
      style={{ width: "100%", minHeight: "100vh", backgroundColor: "#051650" }}
      className="exhibitionPage"
    >
      <ExhibitionSlider />

      <div className="exhibitionPage-textWrapper">
        <div className="container">
          <div className="exhibitionPage-textWrapper-text">
            <img src={borderLeftIcon} alt="" className="exhibitionPage-textWrapper-text-borderLeft" />
            <img src={borderRightIcon} alt="" className="exhibitionPage-textWrapper-text-borderRight" />
            <h1 className="exhibitionPage-title">{text.title}</h1>
            <p className="exhibitionPage-text">{text.descriptions}</p>
            <a target="_blank" rel="noreferrer" href="https://docs.google.com/forms/d/e/1FAIpQLScDj8TFoAkl6C-FfrEMZ0HjUhiLJQ8AqANFC0WD05Y1Nf46pQ/viewform">
            <button
              className="exhibitionPage-btn"

            >
              {
                lang === 'ru'
                ? 'Арендовать стенд'
                : lang === 'en'
                ? 'Rent a stand'
                : 'Стенд ижарага алуу'
              }
            </button>
            </a>

          </div>
        </div>
      </div>
    </div>
  );
};
