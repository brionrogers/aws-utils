import boto3

class SecurityGroupObj:
  def __init__(self, id, name, type, protocol, fromPort, toPort, cidr, cidrRuleDescription, sgId, sgRuleDescription):
    self.id = id
    self.name = name
    self.type = type
    self.protocol = protocol
    self.fromPort = fromPort
    self.toPort = toPort
    self.cidr = cidr
    self.cidrRuleDescription = cidrRuleDescription
    self.sgId = sgId
    self.sgRuleDescription = sgRuleDescription

# Specify profile here
session = boto3.Session(profile_name='production')
# Specify region here, remove arg if you want to query all regions
ec2 = session.client('ec2', region_name='us-east-1')
sgs = ec2.describe_security_groups()

rules = []
print("SG ID, Group Name, Ingress/Egress, Protocol, From Port, To Port, CIDR Ingress, CIDR Rule Description,Linked Security Group ID, SG Rule Description")
for sg in sgs['SecurityGroups']:
    name=sg['GroupName']
    protocol=""
    try:
        id=sg['GroupId']
    except KeyError:
        id=""
    for permission in sg['IpPermissions']:
        if "IpProtocol" in permission:
            try:
                protocol=permission['IpProtocol']
            except KeyError:
                protocol=""
        else:
            protocol=""
        if "FromPort" in permission:
            try:
                fromPort=permission['FromPort']
            except KeyError:
                fromPort=""
        else:
            fromPort=""
        if "ToPort" in permission:
            try:
                toPort=permission['ToPort']
            except KeyError:
                toPort=""
        else:
            toPort=""
        if "IpRanges" in permission:
            if len(permission['IpRanges']) == 0:
                cidr=""
                cidrRuleDescription=""
            else:
                for ip in permission['IpRanges']:
                    try:
                        cidr=ip['CidrIp']
                    except KeyError:
                        cidr=""
                    try:
                        cidrRuleDescription=ip['Description']
                    except KeyError:
                        cidrRuleDescription=""
                    sgObj = SecurityGroupObj(id,name, "Ingress", protocol, fromPort, toPort, cidr, cidrRuleDescription, "", "")
                    rules.append(sgObj)
        else:
            cidr=""
            cidrRuleDescription=""
            sgObj = SecurityGroupObj(id,name, "Ingress",  protocol, fromPort, toPort, cidr, cidrRuleDescription, "", "")
            rules.append(sgObj)
        if "UserIdGroupPairs" in permission:
            for pairs in permission['UserIdGroupPairs']:
                    try:
                        sgId=pairs['GroupId']
                    except KeyError:
                        sgId=""
                    try:
                        sgRuleDescription=pairs['Description']
                    except KeyError:
                        sgRuleDescription=""
                    sgObj = SecurityGroupObj(id,name, "Ingress", protocol, fromPort, toPort, "", "", sgId, sgRuleDescription)
                    rules.append(sgObj)
        else:
            sgId=""
            sgRuleDescription=""
            sgObj = SecurityGroupObj(id,name, "Ingress", protocol, fromPort, toPort, "", "", sgId, sgRuleDescription)
            rules.append(sgObj)


    for egress in sg['IpPermissionsEgress']:
        if "FromPort" in egress:
            try:
                fromPort=egress['FromPort']
            except KeyError:
                fromPort=""
        else:
            fromPort=""
        if "ToPort" in egress:
            try:
                toPort=egress['ToPort']
            except KeyError:
                toPort=""
        else:
            toPort=""
        if "IpRanges" in egress:
            if len(egress['IpRanges']) == 0:
                cidr=""
                cidrRuleDescription=""
            else:
                for ip in egress['IpRanges']:
                    try:
                        cidr=ip['CidrIp']
                    except KeyError:
                        cidr=""
                    try:
                        cidrRuleDescription=ip['Description']
                    except KeyError:
                        cidrRuleDescription=""
                    sgObj = SecurityGroupObj(id,name, "Egress", protocol, fromPort, toPort, cidr, cidrRuleDescription, "", "")
                    rules.append(sgObj)
        else:
            cidr=""
            cidrRuleDescription=""
            sgObj = SecurityGroupObj(id,name, "Egress", protocol, fromPort, toPort, cidr, cidrRuleDescription, "", "")
            rules.append(sgObj)
        if "UserIdGroupPairs" in egress:
            for pairs in egress['UserIdGroupPairs']:
                    try:
                        sgId=pairs['GroupId']
                    except KeyError:
                        sgId=""
                    try:
                        sgRuleDescription=pairs['Description']
                    except KeyError:
                        sgRuleDescription=""
                    sgObj = SecurityGroupObj(id,name, "Egress", protocol, fromPort, toPort, "", "", sgId, sgRuleDescription)
                    rules.append(sgObj)
        else:
            sgId=""
            sgRuleDescription=""
            sgObj = SecurityGroupObj(id,name, "Egress", protocol, fromPort, toPort, "", "", sgId, sgRuleDescription)
            rules.append(sgObj)
for i in rules:
    print(i.id,", ", i.name,", ", i.type,", ", i.protocol,", ",  i.fromPort,", ", i.toPort,", ", i.cidr,", ", i.cidrRuleDescription, ", ", i.sgId, ", ", i.sgRuleDescription)
