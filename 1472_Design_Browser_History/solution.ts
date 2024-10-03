class BrowserHistory {
  historyStack: string[] = []
  homepage = ""
  currentStep = 0;

  constructor(homepage: string) {
      this.homepage = homepage;
      this.historyStack.push(homepage)
  }

  visit(url: string): void {
      this.historyStack = this.historyStack.slice(0, this.currentStep + 1)
      this.historyStack.push(url)
      this.currentStep += 1
  }

  back(steps: number): string {
      this.currentStep = Math.max(0, this.currentStep - steps)
      return this.historyStack[this.currentStep]
  }

  forward(steps: number): string {
      this.currentStep = Math.min(this.historyStack.length - 1, this.currentStep + steps)
      return this.historyStack[this.currentStep]
  }
}

/**
* Your BrowserHistory object will be instantiated and called as such:
* var obj = new BrowserHistory(homepage)
* obj.visit(url)
* var param_2 = obj.back(steps)
* var param_3 = obj.forward(steps)
*/