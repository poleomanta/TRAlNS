import type { DestinationModel } from "./classes";

export class PlanModel {
  destinations: DestinationModel[];

  constructor(destinations: DestinationModel[]) {
    this.destinations = destinations;
  }
}

export function getPlan(): PlanModel {
  // Take plan from local storage or return empty plan
  const planData = localStorage.getItem("plan");
  if (planData) {
    const parsedData = JSON.parse(planData) as DestinationModel[];
    return new PlanModel(parsedData);
  } else {
    return new PlanModel([]);
  }
}

function savePlan(plan: PlanModel): void {
  localStorage.setItem("plan", JSON.stringify(plan.destinations));
}

export function addDestinationToPlan(destination: DestinationModel): void {
  const plan = getPlan();
  plan.destinations.push(destination);
  savePlan(plan);
}

export function removeDestinationFromPlan(position: number): void {
  const plan = getPlan();
  plan.destinations.splice(position, 1);
  savePlan(plan);
}