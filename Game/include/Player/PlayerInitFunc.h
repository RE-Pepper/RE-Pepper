#pragma once

struct PlayerModelInfo;
struct PlayerAnimInfo;

namespace PlayerInitFunc
{

const PlayerModelInfo* getModelInfo();
const PlayerAnimInfo*  getAnimInfo();
void*                  fn_00260620();

} // namespace PlayerInitFunc
