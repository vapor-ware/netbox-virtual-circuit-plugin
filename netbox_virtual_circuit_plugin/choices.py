from utilities.choices import ChoiceSet


class VirtualCircuitStatusChoices(ChoiceSet):
    """List of possible status for a Virtual Circuit."""

    STATUS_PENDING_CONFIGURATION = 'pending-configuration'
    STATUS_CONFIGURED = 'configured'
    STATUS_CONFIGURATION_ERROR = 'configuration-error'
    STATUS_PENDING_DEACTIVATION = 'pending-deactivation'
    STATUS_DEACTIVATED = 'deactivated'

    CHOICES = (
        (STATUS_PENDING_CONFIGURATION, 'Pending Configuration'),
        (STATUS_CONFIGURED, 'Configured'),
        (STATUS_CONFIGURATION_ERROR, 'Configuration Error'),
        (STATUS_PENDING_DEACTIVATION, 'Pending Deactivation'),
        (STATUS_DEACTIVATED, 'Deactivated'),
    )
