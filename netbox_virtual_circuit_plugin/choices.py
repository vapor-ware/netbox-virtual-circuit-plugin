from utilities.choices import ChoiceSet


class VirtualCircuitStatusChoices(ChoiceSet):
    """List of possible status for a Virtual Circuit."""

    STATUS_PENDING_CONFIGURATION = 'pending-configuration'
    STATUS_CONFIGURED = 'configured'
    STATUS_PENDING_DELETION = 'pending-deletion'
    STATUS_CONFIGURATION_ERROR = 'configuration-error'

    CHOICES = (
        (STATUS_PENDING_CONFIGURATION, 'Pending Configuration'),
        (STATUS_CONFIGURED, 'Configured'),
        (STATUS_PENDING_DELETION, 'Pending Deletion'),
        (STATUS_CONFIGURATION_ERROR, 'Configuration Error'),
    )
