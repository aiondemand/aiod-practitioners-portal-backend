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


/**
 * All or part of an AIAsset in downloadable form
 */
export interface Distribution {
    /**
     * The external platform from which this resource originates. Leave empty if this item originates from AIoD. If platform is not None, the platform_resource_identifier should be set as well.
     */
    platform?: any | null;
    /**
     * A unique identifier issued by the external platform that\'s specified in \'platform\'. Leave empty if this item is not part of an external platform. For example, for HuggingFace, this should be the <namespace>/<dataset_name>, and for Openml, the OpenML identifier.
     */
    platform_resource_identifier?: any | null;
    /**
     * The value of a checksum algorithm ran on this content.
     */
    checksum?: any | null;
    /**
     * The checksum algorithm.
     */
    checksum_algorithm?: any | null;
    copyright?: any | null;
    content_url: any | null;
    content_size_kb?: any | null;
    /**
     * The datetime (utc) on which this Distribution was first published on an external platform.
     */
    date_published?: any | null;
    description?: any | null;
    /**
     * The mimetype of this file.
     */
    encoding_format?: any | null;
    name?: any | null;
    /**
     * The technology readiness level (TRL) of the distribution. TRL 1 is the lowest and stands for \'Basic principles observed\', TRL 9 is the highest and stands for \'actual system proven in operational environment\'.
     */
    technology_readiness_level?: any | null;
}

