import React, {useState} from "react";
import {Button, LinearProgress, Typography} from "@mui/material";
import axios from "axios";

export default function UploadForm(){
  const [progress,setProgress]=useState(0);
  const [taskId,setTaskId]=useState("");
  const onFile=(f:any)=>{
    const fd=new FormData(); fd.append("file", f);
    axios.post('/upload', fd, { onUploadProgress: e=>setProgress(Math.round(e.loaded/e.total*100)) })
      .then(r=>setTaskId(r.data.task_id)).catch(()=>alert("Upload failed"));
  };
  return (<div>
    <input type="file" onChange={e=>onFile(e.target.files?.[0])} />
    <LinearProgress variant="determinate" value={progress} />
    <Typography>Task: {taskId}</Typography>
  </div>);
}
