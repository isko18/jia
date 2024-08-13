// import { FirstSection } from "@components/ProjectsSections";
// import bannerImage from "../../img/projectsBanner.png";
import ReactPlayer from "react-player";
import classes from "./ProjectsPage.module.scss";
import ages1 from "../../img/projects-ages/2015.svg";
import ages2 from "../../img/projects-ages/2016.svg";
import ages3 from "../../img/projects-ages/2017.svg";
import ages4 from "../../img/projects-ages/2019.svg";
import ages5 from "../../img/projects-ages/2022.svg";
import projectVideoBorder from "@img/projectsVideoBorder.png";
import projectVideoBorderRight from "@img/projectsVideoBorderRight.png";
import vector_left from "../../img/vector-left.svg";
import vector_right from "../../img/vector-right.svg";
import investPrice from "../../img/investPrice.svg";
import investDiagram from "../../img/investDiagram.svg";
import "./projectsPage.scss";
// import ProjectsPageHero from "./ProjectsPageHero";
// import ProjectsPageProjects from "./ProjectsPageProjects";
// import ProjectsPageInfo from "./ProjectsPageInfo";
import { SwiperSlide, Swiper } from "swiper/react";
import "swiper/css/pagination";
import "swiper/css/navigation";
import "swiper.css";
import image1 from "../../img/sliderImage.png";
import image2 from "../../img/header/emblem.png";
import { useEffect, useState } from "react";
import { useSelector } from "react-redux";
import { SwiperSection } from "@pages/HomePage/HomeSections";
import { useMediaQuery } from "@hooks/usemedia/useMedia";
const getDinamicData = async (url) => {
  const data = (await fetch(url)).json();
  console.log(data);
  return data;
};
export const ProjectsPage = () => {
  const isM = useMediaQuery(
    "screen and (max-width : 769px)"
  );
  console.log(isM,'isM');


  const [loading, setLoading] = useState(true);
  const [data, setData] = useState({});
  const lang = useSelector(s => s.reducer.lang);
  const domain = useSelector(s => s.reducer.domain);
  useEffect(() => {
    (async () => {
      try {
        const result = {};
        const data1 = await getDinamicData(
          `${domain}/${lang}/api/v1/about/about/`
        );
        const data2 = await getDinamicData(
          `${domain}/${lang}/api/v1/about/about_banner/`
        );

        const data4 = await getDinamicData(
          `${domain}/${lang}/api/v1/about/history/`
        );
        const data5 = await getDinamicData(
          `${domain}/${lang}/api/v1/about/history_detail/`
        );
        const data6 = await getDinamicData(
          `${domain}/${lang}/api/v1/about/statistics/`
        );
        const data7 = await getDinamicData(
          `${domain}/${lang}/api/v1/about/gallery/`
        );
        result.about = {
          title: data1[0].title,
          desc: data1[0].descriptions,
        };
        result.banner = {
          title: data2[0].title,
          desc: data2[0].descriptions,
        };
        result.history_lines = data5;
        result.history = data4;
        result.statistics = data6;
        result.images = data7;
        setData(result);
        setLoading(false);
      } catch {
        alert("Данные не загрузились !");
      }
    })();
  }, [lang]);
  return (
    <div
      style={{ width: "100%", minHeight:'100vh', backgroundColor: "#051650" }}
      className="projects_page"
    >
      {!loading ? (
        <>
          <div className={classes.projects_banner_wrap}>
            <section className={classes.projects_banner + " container"}>
              <div className={classes.projects_banner_content}>
                <h1 className={classes.banner_title}>{data.banner.title}</h1>



                <div className={classes.projects_banner_advantages}>
                  {data.statistics.map((item) => {
                    return (
                      <div className={classes.projects_banner_advantages_block}>
                        <div className={classes.content}>
                          <h3 className={classes.projects_banner_title}>
                            {item.title}
                          </h3>
                          <p className={classes.projects_banner_desc}>
                            {item.descriptions}
                          </p>
                        </div>
                      </div>
                    );
                  })}
                </div>
              </div>
            </section>
          </div>

          <section className={classes.about_projects + " container "}>
            <h1 className={"title " + classes.about_project_title}>
              {data.about.title}
            </h1>

            <div className={classes.about_content}>
              <p className={classes.about_text_content} dangerouslySetInnerHTML= {{__html:data.about.desc}}>


              </p>
            </div>
          </section>

          <section className={classes.history + " container"}>
            <h1 className={classes.history_title + " title"}>
              <img src={vector_right} alt="" />
              {data.history[0].title}
              <img src={vector_left} alt="" />
            </h1>
            <p className={classes.history_text}  dangerouslySetInnerHTML= {{__html: data.history[0].descriptions}}>

            </p>
            <div className={classes.history_ages}>
              <p>
              <a href={`#${data.history[0].year_1}`}>
              {data.history[0].year_1}
              </a>
              </p>
              <p>
              <a href={`#${data.history[0].year_2}`}>{data.history[0].year_2}</a>
              </p>
              <p>
                <a href={`#${data.history[0].year_3}`}>
                {
            data.history[0].year_3
          }
                </a>
              </p>
          <p>
            <a href={`#${data.history[0].year_4}`}>
            {
            data.history[0].year_4
          }
            </a>
          </p>
             <p>
             <a href={`#${data.history[0].year_5}`}>{
            data.history[0].year_5
          }</a>
             </p>

            </div>
          </section>

          <section className={classes.history_lines + " container"}>
            {
              data.history_lines.map((item,index)=>{
                const age = item.title.slice(0,4)
                const title_content = item.title.slice(4,item.title.length)
                console.log(title_content,'cont');
                console.log(age,'age');
                if(index%2==0){
                  return(<div id={age} className={classes.history_lines_block}>
                    <h1 className={classes.history_lines_title}>
                      <span>{age}</span> {title_content}
                    </h1>
                    <div className={classes.history_lines_block_content}>
                      <p dangerouslySetInnerHTML={{__html:item.descriptions}}>

                      </p>
                      <div className={classes.history_lines_video}>
                        <div className={classes.history_lines_video_block}>
                        <ReactPlayer
                      width={isM?'100vw':'100%'}
                      height={'100%'}
                      position={'relative'}
                      zIndex={'2'}

                                    url={item.url} controls={true} alt=""/>
                        </div>


                        <img
                          className={classes.history_lines_video_border}
                          alt="history_lines_video_border"
                          src={projectVideoBorder}
                        />
                      </div>
                    </div>
                    <div className={classes.history_lines_footer}>
                      <div className={classes.history_lines_footer_item}>
                        <img src={investPrice} alt="" /> {item.amount_projet}
                      </div>
                      <div className={classes.history_lines_footer_item}>
                        <img src={investDiagram} alt="" /> {item.amount_invest}
                      </div>
                    </div>
                  </div>)
                }
                return (
                  <div id={age} className={classes.history_lines_block}>
                  <h1
                    className={classes.history_lines_title}
                    style={{ textAlign: "end" }}
                  >
                    <span>{age}</span> {title_content}
                  </h1>
                  <div className={classes.history_lines_block_content}>
                    <div className={classes.history_lines_video}>
                    <div className={classes.history_lines_video_block}>
                        <ReactPlayer
                         width={isM?'100vw':'100%'}
                      height={'100%'}
                      position={'relative'}
                      zIndex={'2'}
                                    url={item.url} controls={true} alt=""/>
                        </div>

                      <img
                        className={classes.history_lines_video_border}
                        alt="history_lines_video_border"
                        src={projectVideoBorderRight}
                        style={{ left: "24px" }}
                      />
                    </div>
                    <p dangerouslySetInnerHTML={{__html:item.descriptions}}>

                    </p>
                  </div>
                  <div className={classes.history_lines_footer}>
                    <div className={classes.history_lines_footer_item}>
                      <img src={investPrice} alt="investPrice" /> {item.amount_invest}
                    </div>
                    <div className={classes.history_lines_footer_item}>
                      <img src={investDiagram} alt="investDiagram" /> {item.amount_projet}
                    </div>
                  </div>
                </div>
                )

              })
            }



       </section>
       <SwiperSection />

        </>
      ) : (
        ""
      )}
    </div>
  );
};
