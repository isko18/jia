import { BrowserRouter, Route, Routes } from "react-router-dom";
import { ErrorPage, ExhibitionPage, FundsPage, HomePage, ProjectsPage, BusinessPage, RegistrationPage } from "./pages";
import { Footer, Header, NavigationTop } from "./components";
import { useEffect } from "react";
import axios from "axios";

function App() {function getCsrfToken() {
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
useEffect(() => {
  const csrfToken = getCsrfToken();
  axios.interceptors.request.use((config) => {
    config.headers['X-CSRF-TOKEN'] = csrfToken;
    return config;
  }, (error) => {
    return Promise.reject(error);
  });
}, []);

  return (
    <BrowserRouter >
      <Header />
      <NavigationTop />

      <Routes>
        <Route path="/" element={<HomePage />} />
        <Route path="/:lang" element={<HomePage />} />
        <Route path="/:lang/funds" element={<FundsPage />} />
        <Route path="/:lang/projects" element={<ProjectsPage />} />
        <Route path="/:lang/business" element={<BusinessPage />} />
        <Route path="/:lang/exhibition" element={<ExhibitionPage />} />
        <Route path="/:lang/registration" element={<RegistrationPage />} />
        <Route path="*" element={<ErrorPage />} />
      </Routes>
      <Footer />
    </BrowserRouter>
  );
}

export default App;
