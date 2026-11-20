rule SWS405_Harmless_Ransomware_Simulator
{
    meta:
        description = "Detects the SWS405 harmless ransomware-behaviour training sample"
        author = "SWS405 teaching lab"
        purpose = "Educational demonstration only"

    strings:
        $marker1 = "SIMULATED_RANSOM_NOTE" ascii
        $marker2 = "YOUR FILES ARE LOCKED" ascii
        $marker3 = "No encryption, deletion, persistence" ascii

    condition:
        2 of them
}
