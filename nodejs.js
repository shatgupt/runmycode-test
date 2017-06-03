console.log('Hello World from nodejs!')
// remove node and script path from args to keep output uniform across envs
console.log(`${process.argv.slice(2).length} Args: [${process.argv.slice(2).join(', ')}]`)
