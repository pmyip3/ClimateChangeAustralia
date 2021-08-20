import { VictoryChart, VictoryAxis, VictoryTheme, VictoryLine } from 'victory';
import React, { useState } from 'react';

const Chart = () => {
    const [ data, setData ] = useState([
        {year: 1975, month: 1, value: 123.34},
        {year: 1975, month: 2, value: 254.34},
        {year: 1975, month: 3, value: 214.34},
        {year: 1975, month: 4, value: 236.34},
      ]);
    return(
        <div className="App">
            <VictoryChart 
                theme={VictoryTheme.material}
                width='960'
                height='500'
                domainPadding={50}
                padding={{ top: 10, bottom: 40, left: 80, right: 10}}
            >
                <VictoryAxis
                label="time"
                style={{
                    axisLabel: { padding: 40 }
                }}
                />
                <VictoryAxis dependentAxis
                label="value"
                tickFormat={(x) => x}
                style={{
                    axisLabel: { padding: 40 }
                }}
                />
                <VictoryLine data={data} x={['year', 'month']} y="value" />
            </VictoryChart>
        </div>

    )
}

export default Chart