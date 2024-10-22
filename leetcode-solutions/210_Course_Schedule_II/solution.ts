function findOrder(numCourses: number, prerequisites: number[][]): number[] {
    const adjList: Record<string, number[]> = {}
    prerequisites.forEach(([course, prereq], i) => {
        if (adjList[prereq] === undefined) {
            adjList[prereq] = [course]
        } else {
            adjList[prereq].push(course)
        }
    })
    const firstPrereq = Math.min(...Object.keys(adjList).map(x => +x))

    const result: number[] = []
    const visited = [firstPrereq]
    const queue = [firstPrereq];
    console.log(adjList, firstPrereq)
    // return []

    while (queue.length) {
        const prereq = queue.shift();
        result.push(prereq as number)
        console.log('result', result, queue)

        if (!adjList[String(prereq)]) continue;
        
        adjList[String(prereq)].forEach(course => {
            if (!visited.includes(course)) {
                visited.push(course);
                queue.push(course)
            }
        })
    }

    return result;
};

console.log(
  findOrder(2, [[1,0]])
)