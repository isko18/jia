import { FirstSection } from "./FundsSections";
import classes from './FundPage.module.scss'
import { useEffect, useState } from "react";
import { useSelector } from "react-redux";
export const FundsPage = () => {
    const [data,setData] = useState({})
    const domain = useSelector(s => s.reducer.domain);
    const lang = useSelector(s => s.reducer.lang);

    useEffect(()=>{
        (async()=>{
            const res =await fetch(`${domain}/${lang}/api/v1/financing/financing/`)
            const data_fetch =await res.json()
            if(data_fetch.length){
                setData({...data,title:data_fetch[0].title})
            }
        })()
    },[lang, domain])
    return (
        <div style={{minHeight: '100vh'}} className={classes.fund}>
            <section className={classes.section}>
            <h1 className={classes.title_page}>
            {data.title?data.title:''}
            </h1>
            </section>

            <FirstSection />
        </div>
    );
}
