import axios from "axios";
export const uploadFile = (file: File, onProgress: (n:number)=>void) => {
  const fd = new FormData(); fd.append('file', file);
  return axios.post('/upload', fd, { onUploadProgress: e=>onProgress(Math.round(e.loaded/e.total*100)) });
}
export const getStatus = (taskId: string) => axios.get(`/status/${taskId}`);
