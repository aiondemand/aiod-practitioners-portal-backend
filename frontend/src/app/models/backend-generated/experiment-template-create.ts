/**
 * AIOD - Practitioner\'s Portal
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 0.1.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */
import { TaskType } from './task-type';
import { EnvironmentVarDef } from './environment-var-def';
import { AssetSchema } from './asset-schema';


export interface ExperimentTemplateCreate { 
    name: string;
    description: string;
    task: TaskType;
    datasets_schema: AssetSchema;
    models_schema: AssetSchema;
    envs_required: Array<EnvironmentVarDef>;
    envs_optional: Array<EnvironmentVarDef>;
    available_metrics: Array<string>;
    dockerfile: string;
    script: string;
    pip_requirements: string;
}
export namespace ExperimentTemplateCreate {
}


