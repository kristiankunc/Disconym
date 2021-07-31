const express = require("express");
const {exec} = require("child_process");
const { json } = require("express");

const app = express();

const port = 80;
app.listen(port, () => console.log(`Server running on port ${port}`));

async function get_api(){
    return new Promise((resolve, reject) => {
        exec('python -c "import db_actions; print(db_actions.Database.read_api())"', (error, stdout, stderr) => {
            const api_data_raw = stdout.split("'");

            const total_messages = api_data_raw[1];
            const total_guilds = api_data_raw[3];

            const api_data = {
                total_messages,
                total_guilds
            };
            resolve(api_data);
        });
    });
}

app.get('/', async(req, res) => {
    res.send("Disconym public API")
});

app.get('/all', async(req, res) => {
    const api_data = await get_api();
    res.json(api_data);
});

app.get('/msgs', async(req, res) => {
    const api_data = await get_api();
    res.json(Number(api_data.total_messages));
});

app.get('/guilds', async(req, res) => {
    const api_data = await get_api();
    res.json(Number(api_data.total_guilds));
});