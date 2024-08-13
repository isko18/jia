import {createAction, createReducer} from '@reduxjs/toolkit';

const SET_LANG = "SET_LANG"

const intitialState = {
  lang: 'ru',
  domain: 'https://biforum.kg',
}

export const setLang = createAction(SET_LANG);


export default createReducer(intitialState, (builder) =>{
    builder
    .addCase(SET_LANG, (state, action)=>{
            state.lang = action.payload
    })

})
