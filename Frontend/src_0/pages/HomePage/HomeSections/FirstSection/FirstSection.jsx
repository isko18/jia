import styles from "./FirstSection.module.scss";
import { useState, useEffect } from "react";
import axios from "axios";
import { useSelector } from "react-redux";

export const FirstSection = () => {
  const [data, setData] = useState({});
  const lang = useSelector((s) => s.reducer.lang);
  const domain = useSelector(s => s.reducer.domain);

  useEffect(() => {
    axios(`${domain}/${lang}/api/v1/base/banner/`)
      .then(({ data }) =>{
        data.length > 0
        ?  setData(data[0])
        :  setData({
            image: "",
            title: "",
            descriptions: "",
          });
      })
      .catch(() => {
        setData({
          image: "",
          title: "",
          descriptions: "",
        });
      });
  }, [lang, domain]);
  return (
    <section className={styles.container}>
      <img src={data.image} alt="" />
      <div className={styles.text}>
        <div className={styles.discriptions}>
          <p>{data.title}</p>
        </div>
        <h1>{data.descriptions}</h1>
      </div>
    </section>
  );
};
