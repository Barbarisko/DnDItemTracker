var artifact_api = {
    async get_all_artifacts(character_id) { 
        var artifacts = []
        await fetch(`http://127.0.0.1:5000/api/artifact/get_all/${character_id}`, {
            method: 'GET',
            headers: {
                'Content-type': 'application/json; charset=UTF-8'
            }
        })
        .then(response => {
            // indicates whether the response is successful (status code 200-299) or not
            if (!response.ok) {
                throw new Error(`Request failed with status ${reponse.status}`)
            }
            return response.json()
        })
        .then(data => {
            data.forEach(element => {
                artifacts.push(
                    {
                        id: element["id"],
                        name: element["name"],
                        descr: element["descr"],
                        charges: Array.apply(0, Array(element["charges"])).map(function (x, i) { return i < element["used_charges"]; })
                    }
                )
            });
        })
        .catch(error => console.log(error))
        return artifacts;
    }
  }
  
  export default artifact_api