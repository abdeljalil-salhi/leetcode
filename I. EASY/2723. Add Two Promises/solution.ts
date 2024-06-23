type P = Promise<number>;

async function addTwoPromises(promise1: P, promise2: P): P {
  return Promise.all([promise1, promise2]).then((values) => {
    return values.reduce((partialSum, a) => partialSum + a, 0);
  });
}

/**
 * addTwoPromises(Promise.resolve(2), Promise.resolve(2))
 *   .then(console.log); // 4
 */
