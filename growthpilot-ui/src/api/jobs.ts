const API_URL = "http://127.0.0.1:8000";


export async function fetchJobs() {

  const response = await fetch(
    `${API_URL}/jobs`
  );

  return response.json();
}