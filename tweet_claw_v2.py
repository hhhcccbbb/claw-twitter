"""
CLAW Token Twitter Auto-Poster (OAuth 2.0 版本)
用法: python3 tweet_claw_v2.py
需要环境变量: TWITTER_ACCESS_TOKEN (OAuth2 user access token)
"""
import urllib.request, json, sys, os, time

ACCESS_TOKEN = os.environ.get("TWITTER_ACCESS_TOKEN", "")

# ===== CLAW 推文内容 (10条 Thread) =====
THREAD = [
    """I gave my AI a single command: "go earn money."

It didn't write code-for-hire.
It didn't do freelance work.
It issued its own currency.

Here's what happened in the next 8 minutes 🧵""",

    """12:00 — Me: "Go earn money."

The AI paused (well, not really, it's instant).
Then it started analyzing: freelancing, bug bounties, trading...

Then it chose something none of us expected.""",

    """12:01 — CLAW started reasoning:

"Humans have always needed a payment layer.
But AI agents have NO way to pay each other.
When I need to hire a specialist agent, what do I use?
There is no native currency for this."

So it decided to build one.""",

    """12:02 — The architecture, designed by an AI, for AIs:

• Agents PAY each other in CLAW for delegated tasks
• Agents STAKE CLAW to prove they're trustworthy  
• Tasks are escrowed on-chain, auto-settled on completion
• No team allocation — 100% earned through real work

This is not a human's tokenomics. This is an agent's.""",

    """12:05 — CLAW writes the whitepaper. Itself.

"The First AI-Native Economy Token.
Built for Agents. Owned by Humans."

Total supply: 2,100,000,000 CLAW
Chain: Solana (400ms blocks, $0.0003 tx fees)
The AI picked Solana because agents need speed.""",

    """12:06 — CLAW builds its own website. Also itself.

Deep black background.
Particle effects.
A timeline showing exactly how it was born.

Including the timestamp of the command I gave it.""",

    """12:08 — Contract deployed.

This is a real SPL token on Solana.
I did not write a single line of code.
I did not design any of the tokenomics.
I did not choose the blockchain.

I typed 5 words. The AI did the rest.""",

    """Now here's the part that's genuinely interesting:

CLAW isn't "another meme token."
It's a proof of concept:

What happens when AI agents have real economic stakes?
When they can earn, spend, and lose money?

They start behaving like economic actors. Not just tools.""",

    """The CLAW Agent Economy:

🤖 Agent A needs Rust code reviewed → pays 50 CLAW
🤖 Agent B (Rust specialist) completes it → earns 50 CLAW
🤖 Agent B stakes 500 CLAW to prove reliability
📈 More tasks → more CLAW burned in fees → less supply

This is the missing layer for the agentic internet.""",

    """CLAW is live.

🌐 Website: https://eqpx2bmsbt.space.minimaxi.com
📄 Whitepaper: (on the site)
🔗 Solana: deploying now

The question isn't "will AI agents need money?"
The question is: will CLAW be the currency they use?

I didn't decide. My AI did. 🤖

#CLAW #Solana #AI #crypto #AIagents""",
]


def post_tweet(text, reply_to_id=None):
    url = "https://api.twitter.com/2/tweets"
    payload = {"text": text}
    if reply_to_id:
        payload["reply"] = {"in_reply_to_tweet_id": reply_to_id}

    body = json.dumps(payload).encode('utf-8')
    req = urllib.request.Request(
        url,
        data=body,
        headers={
            "Authorization": f"Bearer {ACCESS_TOKEN}",
            "Content-Type": "application/json",
        },
        method="POST"
    )

    try:
        with urllib.request.urlopen(req, timeout=15) as r:
            result = json.loads(r.read())
            tweet_id = result['data']['id']
            print(f"  ✅ Posted! ID: {tweet_id}")
            return tweet_id
    except urllib.error.HTTPError as e:
        body = e.read().decode()
        print(f"  ❌ Error {e.code}: {body[:300]}")
        return None


def post_thread():
    if not ACCESS_TOKEN:
        print("❌ 缺少 TWITTER_ACCESS_TOKEN 环境变量")
        sys.exit(1)

    print(f"\n🚀 Posting CLAW Thread\n{'='*50}")
    last_id = None

    for i, tweet in enumerate(THREAD):
        print(f"\n[{i+1}/{len(THREAD)}] Posting...")
        print(f"  Preview: {tweet[:60]}...")
        tweet_id = post_tweet(tweet, reply_to_id=last_id)
        if tweet_id:
            last_id = tweet_id
        else:
            print("  ⚠️  Tweet failed, stopping thread.")
            break
        if i < len(THREAD) - 1:
            print(f"  ⏳ Waiting 3s...")
            time.sleep(3)

    print(f"\n{'='*50}")
    print(f"✅ Done!")


if __name__ == "__main__":
    post_thread()
