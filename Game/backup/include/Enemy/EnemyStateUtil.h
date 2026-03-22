#pragma once

namespace al
{
class LiveActor;
}
class EnemyStateBlowDown;

namespace EnemyStateUtil
{

bool tryRequestPressDownAndNextNerve( u32 msg, al::HitSensor* other, al::HitSensor* me, al::LiveActor* actor, const al::Nerve* nextNerve );

bool tryRequestBlowDownAndNextNerve( u32 msg, al::HitSensor* other, al::HitSensor* me, EnemyStateBlowDown* state, const al::Nerve* nextNerve );

} // namespace EnemyStateUtil
