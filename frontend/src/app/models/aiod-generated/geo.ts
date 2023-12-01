/**
 * FastAPI
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 0.1.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */


/**
 * The geographic coordinates of a physical location
 */
export interface Geo { 
    /**
     * The latitude of a location in degrees (WGS84)
     */
    latitude?: any | null;
    /**
     * The longitude of a location in degrees (WGS84)
     */
    longitude?: any | null;
    /**
     * The elevation in millimeters with tespect to the WGS84 ellipsoid
     */
    elevation_millimeters?: any | null;
}

