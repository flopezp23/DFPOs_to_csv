# DFPOs_to_csv
This is a python script to convert a json configuration file into a csv file which will contain all POs information.

V1.0
Important instructions:
**Before to run the script, the json file must contain only ProtectedObjects information so it is required to deleted the ProtectedNetworks section.**

Below an example of the json file:
{
  "protectedObjects" : [ {
    "id" : "61",
    "adminStatus" : "ENABLED",
    "name" : "PO_Name_1",
    "description" : "None",
    "bandwidthBitsPerSecond" : "30000000000",
    "overrideMode" : "AUTOMATIC",
    "enableOverrideMode" : "false",
    "updateTime" : "1717526389240",
    "idle" : "false",
    "protectedNetworks" : [ "128.0.0.0/1"],
    "workflow" : "Workflow_1",
    "overrideGeoFeedGroupEnabled" : false,
    "geoFeedGroupBlock" : true,
    "granularDefenseProDetection" : "false",
    "customThresholdInstanceRaw" : [ ],
    "anomalyDetections" : [ ],
    "protectedObjectTemplate" : {
      "name" : "DF_PO_Name_1",
      "dpVersion" : "8.26.5.0"
    },
    "policyPrecedence" : "3",
    "defaultOperation" : "Alert_1",
    "bgpCommunitiesCustom" : [ ],
    "bgpCommunitiesWellKnown" : [ ],
    "overrideSecurityTemplateEnabled" : "true",
    "overrideTemplate" : {
      "name" : "Security_Template_1",
      "dpVersion" : "8.26.5.0"
    },
    "overrideGracePeriod" : "false",
    "nlriIpv4" : "",
    "nlriIpv6" : "",
    "asPath" : "",
    "azureResourceType" : "IAAS",
    "awsUseCdn" : "false",
    "awsLoadBalancerType" : "APPLICATION",
    "detection" : "Detection-1",
    "summarizationDetails" : {
      "enabled" : false
    }
  }, {
    "id" : "70",
    "adminStatus" : "ENABLED",
    "name" : "PO_Name_2",
    "description" : "None",
    "bandwidthBitsPerSecond" : "30000000000",
    "overrideMode" : "AUTOMATIC",
    "enableOverrideMode" : "false",
    "updateTime" : "1722359299510",
    "idle" : "false",
    "protectedNetworks" : [ "128.1.0.0/1"],
    "workflow" : "Workflow_2",
    "overrideGeoFeedGroupEnabled" : false,
    "geoFeedGroupBlock" : true,
    "granularDefenseProDetection" : "false",
    "customThresholdInstanceRaw" : [ ],
    "anomalyDetections" : [ ],
    "protectedObjectTemplate" : {
      "name" : "DF_PO_Name_2",
      "dpVersion" : "8.26.5.0"
    },
    "policyPrecedence" : "3",
    "defaultOperation" : "Alert_2",
    "bgpCommunitiesCustom" : [ ],
    "bgpCommunitiesWellKnown" : [ ],
    "overrideSecurityTemplateEnabled" : "true",
    "overrideTemplate" : {
      "name" : "Security_Template2",
      "dpVersion" : "8.26.5.0"
    },
    "overrideGracePeriod" : "false",
    "nlriIpv4" : "",
    "nlriIpv6" : "",
    "asPath" : "",
    "azureResourceType" : "IAAS",
    "awsUseCdn" : "false",
    "awsLoadBalancerType" : "APPLICATION",
    "detection" : "Detection-2"
  } ],
  "protectedNetworks" : [ {
    "protectedObject" : "PO_Name_1",
    "network" : "128.0.0.0/1"
  }, {
    "protectedObject" : "PO_Name_2",
    "network" : "128.1.0.0/1"
  }]
}

From the above json data, it is required to delete the "protectedNetwork" information. The new json data should look like:

[ {
    "id" : "61",
    "adminStatus" : "ENABLED",
    "name" : "PO_Name_1",
    "description" : "None",
    "bandwidthBitsPerSecond" : "30000000000",
    "overrideMode" : "AUTOMATIC",
    "enableOverrideMode" : "false",
    "updateTime" : "1717526389240",
    "idle" : "false",
    "protectedNetworks" : [ "128.0.0.0/1"],
    "workflow" : "Workflow_1",
    "overrideGeoFeedGroupEnabled" : false,
    "geoFeedGroupBlock" : true,
    "granularDefenseProDetection" : "false",
    "customThresholdInstanceRaw" : [ ],
    "anomalyDetections" : [ ],
    "protectedObjectTemplate" : {
      "name" : "DF_PO_Name_1",
      "dpVersion" : "8.26.5.0"
    },
    "policyPrecedence" : "3",
    "defaultOperation" : "Alert_1",
    "bgpCommunitiesCustom" : [ ],
    "bgpCommunitiesWellKnown" : [ ],
    "overrideSecurityTemplateEnabled" : "true",
    "overrideTemplate" : {
      "name" : "Security_Template_1",
      "dpVersion" : "8.26.5.0"
    },
    "overrideGracePeriod" : "false",
    "nlriIpv4" : "",
    "nlriIpv6" : "",
    "asPath" : "",
    "azureResourceType" : "IAAS",
    "awsUseCdn" : "false",
    "awsLoadBalancerType" : "APPLICATION",
    "detection" : "Detection-1",
    "summarizationDetails" : {
      "enabled" : false
    }
  }, {
    "id" : "70",
    "adminStatus" : "ENABLED",
    "name" : "PO_Name_2",
    "description" : "None",
    "bandwidthBitsPerSecond" : "30000000000",
    "overrideMode" : "AUTOMATIC",
    "enableOverrideMode" : "false",
    "updateTime" : "1722359299510",
    "idle" : "false",
    "protectedNetworks" : [ "128.1.0.0/1"],
    "workflow" : "Workflow_2",
    "overrideGeoFeedGroupEnabled" : false,
    "geoFeedGroupBlock" : true,
    "granularDefenseProDetection" : "false",
    "customThresholdInstanceRaw" : [ ],
    "anomalyDetections" : [ ],
    "protectedObjectTemplate" : {
      "name" : "DF_PO_Name_2",
      "dpVersion" : "8.26.5.0"
    },
    "policyPrecedence" : "3",
    "defaultOperation" : "Alert_2",
    "bgpCommunitiesCustom" : [ ],
    "bgpCommunitiesWellKnown" : [ ],
    "overrideSecurityTemplateEnabled" : "true",
    "overrideTemplate" : {
      "name" : "Security_Template2",
      "dpVersion" : "8.26.5.0"
    },
    "overrideGracePeriod" : "false",
    "nlriIpv4" : "",
    "nlriIpv6" : "",
    "asPath" : "",
    "azureResourceType" : "IAAS",
    "awsUseCdn" : "false",
    "awsLoadBalancerType" : "APPLICATION",
    "detection" : "Detection-2"
  } ]

You also will find in the repository an example of the input file in the corresponding format, as well as an example of the output file.

