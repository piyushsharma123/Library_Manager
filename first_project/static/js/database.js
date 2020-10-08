(function($) {
const MongoClient = require('mongodb').MongoClient;
const uri = "mongodb+srv://company:123456aA@cluster0-shcvj.mongodb.net/<dbname>?retryWrites=true&w=majority";
const client = new MongoClient(uri, { useNewUrlParser: true });
client.connect(err => {
  const collection = client.db("intern").collection("task_2");
  // perform actions on the collection object
  client.close();
});
})(mongo);
