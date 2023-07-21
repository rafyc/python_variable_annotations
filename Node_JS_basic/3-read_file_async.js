const fs = require('fs/promises');

const countStudents = async (path) => {
  try {
    const data = await fs.readFile(path, { encoding: 'utf8' });

    const removeHeader = data.split('\n');
    removeHeader.shift();
    const cleanArr = removeHeader.filter((e) => e);
    let num = cleanArr.length;

    console.log(`Number of students: ${num}`);

    const all = cleanArr.map((el) => el.split(','));

    const spe = ['CS', 'SWE'];

    spe.forEach((el) => {
      const studentsWithField = all.filter((e) => e[3] === el);
      const names = studentsWithField.map((e) => e[0]).join(', ');
      console.log(`Number of students in ${el}: ${studentsWithField.length}. List: ${names}`);
    });
  } catch (e) {
    throw new Error('Cannot load the database');
  }
};

module.exports = countStudents;
