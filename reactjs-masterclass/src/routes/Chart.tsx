import { string } from "prop-types";
import ReactApexChart from "react-apexcharts";
import { useQuery } from "react-query";
import { useRecoilValue } from "recoil";
import { fetchChart } from "../api";
import { isDarkAtom } from "../atoms";


interface IChart {
    coinId: string
}

interface IHistoricalData {
    time_open: number,
    time_close: number,
    open: string,
    high: string,
    low: string,
    close: string,
    volume: string,
    market_cap: number
}

function Chart({ coinId }: IChart) {
    const { isLoading, data } = useQuery<IHistoricalData[]>(["chart", coinId], () => fetchChart({ coinId }));
    const isDark = useRecoilValue(isDarkAtom);
    return <div>
        {isLoading ? "Loading Chart..." :
            <ReactApexChart
                type="line"
                series={[
                    {
                        name: "sales",
                        /* fetch로 부터 undefined 데이터 타입이 들어올 수 있기 때문에
                        as Number[]로 강제 형변환 해주어야한다. */
                        data: data?.map((price) => parseFloat(price.close)) as number[]
                    }
                ]}
                options={{
                    theme: {
                        mode: isDark ? "dark" : "light"
                    },
                    chart: {
                        height: 500,
                        width: 500
                    }
                }} />
        }
    </div>
}

export default Chart;