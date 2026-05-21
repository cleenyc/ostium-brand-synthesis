> ## Documentation Index
> Fetch the complete documentation index at: https://docs.ostium.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Connect Your Account

> Get started on Ostium with email login or Web3 wallet. Choose your preferred connection method and enable 1-click trading.

## Overview

Ostium offers two ways to connect: email login (smart account) or Web3 wallet. Both methods are non-custodial. Trading is settled on <Tooltip tip="An Ethereum Layer 2 network with sub-second finality and low gas costs.">Arbitrum</Tooltip>.

| Feature         | Email Login                        | Web3 Wallet        |
| --------------- | ---------------------------------- | ------------------ |
| Setup time      | \~30 seconds                       | \~1 minute         |
| Gas fees        | Platform-sponsored (no ETH needed) | You pay gas in ETH |
| Custody         | Smart account on Arbitrum          | Your own wallet    |
| 1-click trading | Built-in                           | Enable separately  |

## How to Connect

<Tabs>
  <Tab title="Email Login" icon="envelope">
    Email login creates a smart account on Arbitrum, managed by you but with gasless transactions. Your funds remain under your control; Privy manages the account infrastructure without accessing your keys.

    <Steps>
      <Step title="Open app.ostium.com and click Connect">
        Open [app.ostium.com](https://app.ostium.com) and click "Connect."
      </Step>

      <Step title="Select Email">
        Choose the "Email" option.
      </Step>

      <Step title="Enter your email address">
        Type your email address.
      </Step>

      <Step title="Check your inbox for verification code">
        Look for a code from [no-reply@privy.io](mailto:no-reply@privy.io). Check spam if it doesn't arrive within a minute.
      </Step>

      <Step title="Paste the verification code">
        Copy the code and paste it back into Ostium.
      </Step>

      <Step title="Account created">
        Your smart account is created and ready to fund. Your address appears in your profile.
      </Step>
    </Steps>

    <Note>
      Smart accounts deduct 2 USDC from your balance to ensure you can always withdraw. This covers gas fees for future withdrawal transactions.
    </Note>
  </Tab>

  <Tab title="Web3 Wallet" icon="wallet">
    Web3 wallet connection gives you full self-custody via your own Arbitrum-compatible wallet (MetaMask, Rabby, Coinbase Wallet, etc.).

    <Steps>
      <Step title="Open app.ostium.com and click Connect">
        Open [app.ostium.com](https://app.ostium.com) and click "Connect."
      </Step>

      <Step title="Select Continue with a wallet">
        Choose "Continue with a wallet."
      </Step>

      <Step title="Choose your wallet provider">
        Select MetaMask, Coinbase, Rabby, or another supported wallet.
      </Step>

      <Step title="Approve the connection">
        Approve the connection request in your wallet.
      </Step>

      <Step title="Switch to Arbitrum if prompted">
        If your wallet is on a different network, switch to Arbitrum when prompted.
      </Step>

      <Step title="Connection complete">
        Your wallet address appears in the app. You're ready to fund.
      </Step>
    </Steps>

    Your funds stay in your wallet at all times. The Ostium smart contracts are permitted to interact with them only for trades you authorize.
  </Tab>
</Tabs>

## Enable 1-Click Trading

<Info>
  1-click trading pre-approves transactions so Ostium can execute trades faster without requiring manual approval for each order.
</Info>

<Tabs>
  <Tab title="Web3 Wallet" icon="wallet">
    <Steps>
      <Step title="Go to your profile settings">
        Open your profile settings page.
      </Step>

      <Step title="Enable 1-Click Trading">
        Find "1-Click Trading" and click to enable.
      </Step>

      <Step title="Approve the required transactions">
        Follow the module steps and approve in your wallet. Requires a small amount of ETH for gas.
      </Step>
    </Steps>

    Once enabled, future trades execute without additional prompts. Disable anytime from your profile.
  </Tab>

  <Tab title="Email Login" icon="envelope">
    1-click trading is built into your smart account and enabled by default. No setup needed. Trades are pre-approved automatically, with no gas costs.
  </Tab>
</Tabs>

## Security & Non-Custody

Both connection methods are non-custodial. With email login, Privy manages the smart account infrastructure but cannot access your funds; only you can authorize transactions. With Web3 wallet login, you hold your private keys and full control. In both cases, Ostium never stores or accesses your authentication credentials or keys.

<Warning>
  Only send Arbitrum USDC to your account address. Sending other tokens or using a different chain risks permanent loss of funds.
</Warning>

## Troubleshooting

**Email verification code not arriving?** Check your spam folder. If still missing, wait 5 minutes and request a new code. Privy support is available at [Privy Help](https://privy.io).

**Wallet connection fails?** Ensure your wallet is on Arbitrum network. Try disconnecting and reconnecting. If issues persist, clear your browser cache and try a different wallet or browser.

**Not enough ETH for gas?** Web3 wallet users need a small amount of ETH on Arbitrum to approve transactions and execute trades. If your transactions are failing, check your ETH balance. You can bridge ETH to Arbitrum using the [Arbitrum Bridge](https://bridge.arbitrum.io/) or buy ETH directly on Arbitrum through an exchange that supports Arbitrum withdrawals. Gas fees are typically under \$0.01 per transaction, so even a few dollars of ETH will last a long time.

## FAQ

<Accordion title="Which login method is better for me?">
  Email login requires no gas fees and includes built-in 1-click trading. Web3 wallet provides full self-custody.
</Accordion>

<Accordion title="Can I switch between email and wallet login?">
  No. Email and Web3 wallet logins create separate accounts. You cannot merge them. If you want to use a different method, create a new account.
</Accordion>

<Accordion title="Is my account the same across devices?">
  Yes, if you use the same login method (same email or same wallet). Your balance and positions sync across all devices automatically.
</Accordion>

<Accordion title="Do I need to know about gas fees?">
  With email login, no; all gas fees are covered. With Web3 wallet, you pay small gas fees in ETH for transactions (approval, trades). Arbitrum gas is typically under \$0.01 per transaction.
</Accordion>

## What to Read Next

* **[Fund Your Account](/traders/getting-started/fund-account)** — Deposit USDC on Arbitrum.
* **[Opening a Trade](/traders/trading/opening-a-trade)** — Execute your first order.
