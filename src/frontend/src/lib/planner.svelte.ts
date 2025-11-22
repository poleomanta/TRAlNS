import { X } from "@lucide/svelte";
import type { DestinationModel } from "./classes";
import { browser } from "$app/environment";



export class PlanModel {
  destinations: DestinationModel[];

  constructor(destinations: DestinationModel[]) {
    this.destinations = destinations;
  }
}

export function getPlan(): PlanModel {
  if (!browser || typeof localStorage === undefined) new PlanModel([]);
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
  if (!browser || typeof localStorage === undefined) return;
  localStorage.setItem("plan", JSON.stringify(plan.destinations));
}

export function addDestinationToPlan(destination: DestinationModel): void {
  const plan = getPlan();
  plan.destinations.push(destination);
  savePlan(plan);
}

export function removeDestinationFromPlanByDestination(destination: DestinationModel): void {
  const plan = getPlan();
  plan.destinations = plan.destinations.filter(dest => JSON.stringify(dest) !== JSON.stringify(destination));
  savePlan(plan);
}

export function removeDestinationFromPlan(position: number): void {
  const plan = getPlan();
  plan.destinations.splice(position, 1);
  savePlan(plan);
}

export function isInPlan(destination: DestinationModel): boolean {
  return getPlan().destinations.filter((x) => JSON.stringify(x) == JSON.stringify(destination)).length > 0;
}