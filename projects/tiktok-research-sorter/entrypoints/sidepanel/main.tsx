import React from 'react';
import ReactDOM from 'react-dom/client';
import App from './App';
import VideoDownloadControls from './VideoDownloadControls';
import './style.css';

ReactDOM.createRoot(document.getElementById('root')!).render(
  <React.StrictMode>
    <App />
    <VideoDownloadControls />
  </React.StrictMode>,
);
