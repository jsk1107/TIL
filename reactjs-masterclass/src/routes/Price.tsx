import ReactApexChart from "react-apexcharts";
import { useQuery } from "react-query";
import { fetchChart } from "../api";

interface IPrice {
    coinId: string
}

function Price({ coinId }: IPrice) {
    const { isLoading, data } = useQuery(["price", coinId], () => fetchChart({ coinId }));

    return <div>
        {isLoading ? "Loading price..." :
            <ReactApexChart
                type="bar"
                series={[{
                    data: [{
                        x: 'category A',
                        y: 10
                    }, {
                        x: 'category B',
                        y: 18
                    }, {
                        x: 'category C',
                        y: 13
                    }]
                }]}
                options={{
                    chart: {
                        height: 500,
                        width: 500
                    },

                }}
            />}
    </div>
}

export default Price;