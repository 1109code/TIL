import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import App from './App';
import reportWebVitals from './reportWebVitals';

import Library from './chapter_03/Library';
import Clock from './chapter_04/Clock';
import CommentList from './chapter_05/CommentList';
import NotificationList from './chapter_06/NotificationList';
import Accommodate from './chapter_07/Accommodatte';

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <Accommodate />
  </React.StrictMode>
)

// ReactDOM.createRoot(document.getElementById('root'));
// Chapter 6
// root.render(
//   // <React.StrictMode>
//     <NotificationList />
//   // </React.StrictMode>
// )
// Chapter 5
// root.render(
//   <React.StrictMode>
//     <CommentList />
//   </React.StrictMode>
// );

// Chapter 4
// setInterval(() => {
//   root.render(
//     <React.StrictMode>
//       <Clock />
//     </React.StrictMode>
//   );
// }, 1000);

//Chapter 3
// root.render(
//   <React.StrictMode>
//     <Library />
//   </React.StrictMode>
// );

// ReactDOM.render(
//   <React.StrictMode>
//     <Library />
//   </React.StrictMode>,
//   document.getElementById('root')
// )

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
