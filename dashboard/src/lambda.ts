const { InvokeCommand, LambdaClient } = require("@aws-sdk/client-lambda");
const { fromEnv } = require("@aws-sdk/credential-providers");
require("dotenv").config();

const url =
  "http://capegrim.csiro.au/GreenhouseGas/data/CapeGrim_CO2_data_download.csv";

async function callLambda() {
    try {
      const client = new LambdaClient({ region: "ap-southeast-2", credentials: fromEnv() });
      const encoder = new TextEncoder();
      const payload = encoder.encode(`{ "url": "${url}" }`);
      const command = new InvokeCommand({
        FunctionName: "read_ghg_data",
        Payload: payload,
        InvocationType: "RequestResponse"
      });
      const response = await client.send(command);
      console.log(response);
      const decoder = new TextDecoder('utf-8');
      console.log(decoder.decode(response.Payload));
    } catch (err) {
      console.log(err);
    }
}

callLambda();