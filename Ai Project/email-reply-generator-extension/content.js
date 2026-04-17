console.log("Email Reply Extension content script loaded.");

function createAiButton() {
    const button = document.createElement('div');
    button.className = 'T-I J-J5-Ji aoO v7 T-I-atl L3';
    button.style.marginRight = '8px';
    button.innerHTML = 'AI Reply';
    button.setAttribute('role', 'button');
    button.setAttribute('data-tooltip', 'Generate AI Reply');
    return button;
}

function getEmailContent() {
     const selectors = [
        '.h7',
        '.a3s.aiL',
        '.gmail_quote',
        '[role="presentation"]'
    ];
    for (const selector of selectors) {
        const content = document.querySelector(selector);
        if (content) {
            return content.innerText.trim();
        }
    }
    return '';
}
function findComposeToolbar() {
    const composeWindows = ['.btC', '.aDh', 'role="toolbar"', '.gU.Up'];
    for (const selector of composeWindows) {
        const toolbar = document.querySelector(selector);
        if (toolbar) {
            return toolbar;
        }
    }
        return null;
}
function injectReplyButton() {
    const existingButton = document.querySelector('.email-reply-extension-button');
    if (existingButton) {
        existingButton.remove();
    }
    const toolBar = findComposeToolbar();
    if (!toolBar) {
        console.log("Toolbar not found. Cannot inject reply button.");
        return;
    }

    console.log("Toolbar found. Injecting reply button.");
    const button = createAiButton();
    button.classList.add('email-reply-extension-button');
    button.addEventListener('click', async () => {
        try {
            button.innerHTML = 'Generating...';
            button.disabled = true;
            const response = await fetch('http://localhost:8080/api/email/generate', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    emailContent: getEmailContent(),
                    tone: "professional"
                })
            });
            if (!response.ok) {
                throw new Error('API fetch Failed');
            }
            const generatedReply = await response.text();
            const composeBox = document.querySelector('[role="textbox"][g_editable="true"]');

            if (composeBox) {
                composeBox.focus();
                document.execCommand('insertText', false, generatedReply);  
            }
            else {
                console.error("Compose box not found. Cannot insert generated reply.");
            }
        }
        catch (error) {
            alert("Error generating reply: " + error.message);
        }
        finally {
            button.innerHTML = 'Generate AI Reply';
            button.disabled = false;
        }
    });
    toolBar.insertBefore(button, toolBar.firstChild);
}
const observer = new MutationObserver((mutations) => {
    for (const mutation of mutations) {
        const addedNodes = Array.from(mutation.addedNodes);
        const hasComposeElements = addedNodes.some(node =>
            node.nodeType === Node.ELEMENT_NODE &&
            (node.matches('.aDh, .btC, [role="dialog"]') || node.querySelector('.aDh, .btC, [role="dialog"]'))
        );
        if (hasComposeElements) {
            console.log("Compose window detected. Injecting reply button.");
            setTimeout(injectReplyButton, 1000); // Delay to ensure the compose window is fully loaded
        }
    }
});

observer.observe(document.body, { childList: true, subtree: true }); 