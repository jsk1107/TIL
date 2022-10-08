import { useParams } from "react-router-dom";
import { useEffect} from "react";

function Detail(){
    const {id} = useParams();

    const getMovieDetail = async() =>{
        const response = await fetch(`https://yts.mx/api/v2/movie_details.json?movie_id=${id}`)
        const json = await response.json();
    };

    useEffect(() => {
        getMovieDetail();
    }, []);

    return <h1>Detail</h1>
}

export default Detail;