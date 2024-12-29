function transform(line) {
    var values = line.split(',');
    var obj = new Object();
    obj.ID = values[0];
    obj.Batter = values[1];
    obj.Matches = values[2];
    obj.Innings = values[3];
    obj.Runs = Number(values[4]);
    obj.Avg = parseFloat(values[5]);
    var jsonString = JSON.stringify(obj);
    return jsonString;
   }