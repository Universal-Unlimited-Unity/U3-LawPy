from LawClass import Law
law = [
    "For the purposes of this Act, a public authority is any body exercising governmental functions.",
    "Personal data means any information relating to an identified or identifiable natural person.",
    "Processing refers to any operation performed on personal data, whether automated or not.",
    "A data controller is the entity that determines the purposes and means of processing personal data.",
    "A data processor is a person who processes personal data on behalf of the controller.",

    "The controller must ensure that personal data is processed lawfully and transparently.",
    "The controller must implement appropriate technical and organizational security measures.",
    "Public authorities are required to respond to access requests within the statutory period.",
    "Employees must receive adequate training regarding data protection obligations.",
    "The processor shall act only on documented instructions from the controller.",

    "It is prohibited to process personal data without a valid legal basis.",
    "No person shall disclose confidential information obtained through official duties.",
    "Personal data shall not be retained longer than necessary for the stated purpose.",
    "Unauthorized access to information systems is forbidden.",
    "The transfer of personal data to third parties without authorization is prohibited.",

    "Any person who unlawfully processes personal data shall be subject to administrative fines.",
    "Failure to comply with security obligations shall result in suspension of processing activities.",
    "A controller who violates this Act may be ordered to pay compensation to affected persons.",
    "Repeated violations shall give rise to increased penalties.",
    "Noncompliance with enforcement orders shall be punishable by additional sanctions.",

    "This Act shall not apply where processing is carried out for national security purposes.",
    "Disclosure obligations do not apply where legal professional privilege exists.",
    "Access rights may be restricted where disclosure would seriously impair an ongoing investigation.",
    "The obligation to erase data shall not apply where retention is required by law.",
    "Processing may continue without consent in cases of vital interest of the data subject.",

    "A fine may be imposed for each day of continued noncompliance.",
    "Except in cases of emergency, inspections shall be announced in advance.",
    "A controller is not liable where the damage was caused by an unforeseeable external event.",
    "Any sanction imposed must be proportionate to the severity of the infringement.",
    "Except as otherwise provided by law, enforcement decisions shall be immediately applicable."
]

law = Law(law)
law.DESC()

