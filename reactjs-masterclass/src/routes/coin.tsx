import styled from "styled-components"
import { useParams } from "react-router-dom";


interface IParams {
    coinId: string
}

function Coin() {
    const { coinId } = useParams<IParams>();
    return <h1>Coin: {coinId}</h1>
}

export default Coin