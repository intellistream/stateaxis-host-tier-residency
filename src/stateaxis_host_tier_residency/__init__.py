"""Exact activation contract for bounded StateAxis host-tier residency."""

from __future__ import annotations

from dataclasses import dataclass

MOD_ID = "org.vllm-hust.stateaxis-host-tier-residency"


@dataclass(frozen=True, slots=True)
class HostTierResidencyConfig:
    """The only host-tier authority contract admitted by StateAxis."""

    enabled: bool = True
    max_resident_states: int = 2
    generation_bound: bool = True
    location_epoch_required: bool = True
    snapshot_sha256_required: bool = True
    exact_byte_accounting: bool = True
    transactional_transitions: bool = True
    response_first_offload: bool = True
    prefetch_enabled: bool = False
    fail_closed: bool = True

    def __post_init__(self) -> None:
        if self != HostTierResidencyConfig.__new_default():
            raise ValueError(
                "host-tier residency requires the reviewed bounded contract"
            )

    @classmethod
    def __new_default(cls) -> HostTierResidencyConfig:
        instance = object.__new__(cls)
        for field, value in (
            ("enabled", True),
            ("max_resident_states", 2),
            ("generation_bound", True),
            ("location_epoch_required", True),
            ("snapshot_sha256_required", True),
            ("exact_byte_accounting", True),
            ("transactional_transitions", True),
            ("response_first_offload", True),
            ("prefetch_enabled", False),
            ("fail_closed", True),
        ):
            object.__setattr__(instance, field, value)
        return instance


def host_tier_residency() -> HostTierResidencyConfig:
    """Return the default-off candidate's admitted ON configuration."""

    return HostTierResidencyConfig()


__all__ = ["MOD_ID", "HostTierResidencyConfig", "host_tier_residency"]
