/**
 * AIoD Metadata Catalogue
 * This is the Swagger documentation of the AIoD Metadata Catalogue. For the Changelog, refer to <a href=\"https://github.com/aiondemand/AIOD-rest-api/releases\">https://github.com/aiondemand/AIOD-rest-api/releases</a>.
 *
 * The version of the OpenAPI document: 1.2.20231219
 *
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */
import { Text } from './text';
import { AIoDEntryRead } from './aio-d-entry-read';


export interface EducationalResourceRead {
    /**
     * The external platform from which this resource originates. Leave empty if this item originates from AIoD. If platform is not None, the platform_resource_identifier should be set as well.
     */
    platform?: any | null;
    /**
     * A unique identifier issued by the external platform that\'s specified in \'platform\'. Leave empty if this item is not part of an external platform. For example, for HuggingFace, this should be the <namespace>/<dataset_name>, and for Openml, the OpenML identifier.
     */
    platform_resource_identifier?: any | null;
    name: any | null;
    /**
     * The datetime (utc) on which this resource was first published on an external platform. Note the difference between `.aiod_entry.date_created` and `.date_published`: the former is automatically set to the datetime the resource was created on AIoD, while the latter can optionally be set to an earlier datetime that the resource was published on an external platform.
     */
    date_published?: any | null;
    /**
     * Url of a reference Web page that unambiguously indicates this resource\'s identity.
     */
    same_as?: any | null;
    /**
     * An approximate or recommendation of the time required to use or complete the educational resource.
     */
    time_required?: any | null;
    /**
     * The primary mode of accessing this educational resource.
     */
    access_mode?: any | null;
    /**
     * This resource can be identified by its own identifier, but also by the resource_identifier.
     */
    ai_resource_identifier?: any | null;
    aiod_entry?: AIoDEntryRead;
    /**
     * An alias for the item, commonly used for the resource instead of the name.
     */
    alternate_name?: any | null;
    /**
     * The objective of this AI resource.
     */
    application_area?: any | null;
    /**
     * Contact information of persons/organisations that can be contacted about this resource.
     */
    contact?: any | null;
    content?: Text;
    /**
     * Contact information of persons/organisations that created this resource.
     */
    creator?: any | null;
    description?: Text;
    /**
     * The level or levels of education for which this resource is intended.
     */
    educational_level?: any | null;
    has_part?: any | null;
    /**
     * The language(s) of the educational resource, in ISO639-3.
     */
    in_language?: any | null;
    /**
     * A business domain where a resource is or can be used.
     */
    industrial_sector?: any | null;
    is_part_of?: any | null;
    /**
     * Keywords or tags used to describe this resource, providing additional context.
     */
    keyword?: any | null;
    location?: any | null;
    /**
     * Images or videos depicting the resource or associated with it.
     */
    media?: any | null;
    /**
     * Notes on this AI resource.
     */
    note?: any | null;
    /**
     * The high-level study schedule available for this educational resource. \"self-paced\" is mostly used for MOOCS, Tutorials and short courses without interactive elements; \"scheduled\" is used for scheduled courses with interactive elements that is not a full-time engagement; \"full-time\" is used for programmes or intensive courses that require a full-time engagement from the student.
     */
    pace?: any | null;
    /**
     * Minimum or recommended requirements to make use of this educational resource.
     */
    prerequisite?: any | null;
    /**
     * URLs of relevant resources. These resources should not be part of AIoD (use relevant_resource otherwise). This field should only be used if there is no more specific field.
     */
    relevant_link?: any | null;
    relevant_resource?: any | null;
    relevant_to?: any | null;
    /**
     * The research area is similar to the scientific_domain, but more high-level.
     */
    research_area?: any | null;
    /**
     * The scientific domain is related to the methods with which an objective is reached.
     */
    scientific_domain?: any | null;
    /**
     * The intended users of this educational resource.
     */
    target_audience?: any | null;
    /**
     * The type of educational resource.
     */
    type?: any | null;
    identifier: any | null;
}

